Add your new apps to your git remotes. Make sure to name one remote pro (for “production”) and the other stage (for “staging”):
   - git remote add pro git@heroku.com:YOUR_APP_NAME.git
   - git remote add stage git@heroku.com:YOUR_APP_NAME.git

For staging: git push stage master
For production: git push pro master

Heroku Settings
---------------

For staging
    $ heroku config:set APP_SETTINGS=config.StagingConfig --remote stage

For production:
    $ heroku config:set APP_SETTINGS=config.ProductionConfig --remote pro

Staging:
    $ heroku run python app.py --app wordcounts-stage

Production:
    $ heroku run python app.py --app wordcounts-pro

Local Migration
---------------

We are going to use Alembic and Flask-Migrate to migrate our database to the
latest version. Alembic is migration library for SQLAlchemy and could be used
without Flask-Migrate if you want. However Flask-Migrate does help with some of
the setup and makes things easier.