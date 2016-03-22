"""empty message

Revision ID: 18aef9562946
Revises: None
Create Date: 2016-03-22 16:50:02.265459

"""

# revision identifiers, used by Alembic.
import sil_fhir_server

revision = '18aef9562946'
down_revision = None

from alembic import op
import sqlalchemy as sa



def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Age',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('code', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('system', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('unit', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('value', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('comparator', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Annotation',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('authorString', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('text', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('time', sil_fhir_server.data_types.primitives.DateTimeField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Attachment',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('contentType', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('creation', sil_fhir_server.data_types.primitives.DateTimeField(), nullable=True),
    sa.Column('data', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('hash', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('language', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('size', sil_fhir_server.data_types.primitives.IntegerField(), nullable=True),
    sa.Column('title', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('url', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Coding',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('code', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('display', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('system', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('userSelected', sil_fhir_server.data_types.primitives.BooleanField(), nullable=True),
    sa.Column('version', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Count',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('code', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('system', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('unit', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('value', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('comparator', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Distance',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('code', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('system', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('unit', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('value', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('comparator', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Duration',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('code', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('system', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('unit', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('value', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('comparator', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Money',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('code', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('system', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('unit', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('value', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('comparator', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Period',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('end', sil_fhir_server.data_types.primitives.DateTimeField(), nullable=True),
    sa.Column('start', sil_fhir_server.data_types.primitives.DateTimeField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Quantity',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('code', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('system', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('unit', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('value', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('comparator', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('SimpleQuantity',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('code', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('system', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('unit', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('value', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('comparator', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Address',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('city', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('country', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('district', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('line', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('period', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('postalCode', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('state', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('text', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('type', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('use', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.ForeignKeyConstraint(['period'], ['Period.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('CodeableConcept',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('coding', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('text', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.ForeignKeyConstraint(['coding'], ['Coding.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ContactPoint',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('period', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('rank', sil_fhir_server.data_types.primitives.IntegerField(), nullable=True),
    sa.Column('system', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('use', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('value', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.ForeignKeyConstraint(['period'], ['Period.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('HumanName',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('family', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('given', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('period', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('prefix', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('suffix', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('text', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('use', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.ForeignKeyConstraint(['period'], ['Period.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Range',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('high', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('low', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.ForeignKeyConstraint(['high'], ['Quantity.id'], ),
    sa.ForeignKeyConstraint(['low'], ['Quantity.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Ratio',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('denominator', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('numerator', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.ForeignKeyConstraint(['denominator'], ['Quantity.id'], ),
    sa.ForeignKeyConstraint(['numerator'], ['Quantity.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('SampledData',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('data', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('dimensions', sil_fhir_server.data_types.primitives.IntegerField(), nullable=True),
    sa.Column('factor', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('lowerLimit', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('origin', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('period', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('upperLimit', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.ForeignKeyConstraint(['origin'], ['Quantity.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Signature',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('blob', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('contentType', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('type', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('when', sil_fhir_server.data_types.primitives.DateTimeField(), nullable=True),
    sa.Column('whoUri', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.ForeignKeyConstraint(['type'], ['Coding.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Identifier',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('period', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('system', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('type', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('use', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('value', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.ForeignKeyConstraint(['period'], ['Period.id'], ),
    sa.ForeignKeyConstraint(['type'], ['CodeableConcept.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('TimingRepeat',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('boundsPeriod', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('boundsQuantity', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('boundsRange', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('count', sil_fhir_server.data_types.primitives.IntegerField(), nullable=True),
    sa.Column('duration', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('durationMax', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('durationUnits', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('frequency', sil_fhir_server.data_types.primitives.IntegerField(), nullable=True),
    sa.Column('frequencyMax', sil_fhir_server.data_types.primitives.IntegerField(), nullable=True),
    sa.Column('period', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('periodMax', sil_fhir_server.data_types.primitives.DecimalField(), nullable=True),
    sa.Column('periodUnits', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('when', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.ForeignKeyConstraint(['boundsPeriod'], ['Period.id'], ),
    sa.ForeignKeyConstraint(['boundsQuantity'], ['Quantity.id'], ),
    sa.ForeignKeyConstraint(['boundsRange'], ['Range.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Timing',
    sa.Column('id', sil_fhir_server.data_types.primitives.StringField(), nullable=False),
    sa.Column('code', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.Column('event', sil_fhir_server.data_types.primitives.DateTimeField(), nullable=True),
    sa.Column('repeat', sil_fhir_server.data_types.primitives.StringField(), nullable=True),
    sa.ForeignKeyConstraint(['code'], ['CodeableConcept.id'], ),
    sa.ForeignKeyConstraint(['repeat'], ['TimingRepeat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Timing')
    op.drop_table('TimingRepeat')
    op.drop_table('Identifier')
    op.drop_table('Signature')
    op.drop_table('SampledData')
    op.drop_table('Ratio')
    op.drop_table('Range')
    op.drop_table('HumanName')
    op.drop_table('ContactPoint')
    op.drop_table('CodeableConcept')
    op.drop_table('Address')
    op.drop_table('SimpleQuantity')
    op.drop_table('Quantity')
    op.drop_table('Period')
    op.drop_table('Money')
    op.drop_table('Duration')
    op.drop_table('Distance')
    op.drop_table('Count')
    op.drop_table('Coding')
    op.drop_table('Attachment')
    op.drop_table('Annotation')
    op.drop_table('Age')
    ### end Alembic commands ###
