from flask.views import View
from app import app


class ListView(View):
    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)


class ShowPatients(View):

    def get_template_name(self):
        return patients.html

    def get_objects(self):
        return Patients.query.all()


app.add_url_rule('/patients/', view_func=ShowPatients.as_view('show_patients'))