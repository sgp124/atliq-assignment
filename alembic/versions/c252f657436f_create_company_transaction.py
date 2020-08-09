"""create company_transaction

Revision ID: c252f657436f
Revises: 42fc3e51232a
Create Date: 2020-08-09 15:37:37.428428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c252f657436f'
down_revision = '42fc3e51232a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'company_transcation',
        sa.Column('store',sa.String(20)),
        sa.Column('date',sa.DateTime),
        sa.Column('trans_id',sa.String(20),primary_key=True),
        sa.Column('coustmer_id',sa.String(20)),
        sa.Column('imei', sa.String(20)),
        sa.Column('phone', sa.String(20)),
        sa.Column('trans_type',sa.String(20)),
        sa.Column('state',sa.String(20))
    )
    pass


def downgrade():
    op.drop_table('company_transcation')
    pass
