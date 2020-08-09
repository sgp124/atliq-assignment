"""create mapping table

Revision ID: 3ee1b53e0261
Revises: c252f657436f
Create Date: 2020-08-09 16:58:28.004758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ee1b53e0261'
down_revision = 'c252f657436f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'mapping',
        sa.Column('id', sa.Integer, primary_key=True,autoincrement=True),
        sa.Column('date', sa.DateTime),
        sa.Column('cost', sa.String(20)),
        sa.Column('imei', sa.String(20)),
        sa.Column('phone', sa.String(20)),
        sa.Column('sales_type',sa.Numeric),
        sa.Column('trans_id',sa.String(20)),
        sa.Column('coustmer_id',sa.String(20)),
        sa.Column('store',sa.String(20)),
        sa.Column('trans_type',sa.String(20)),
        sa.Column('state',sa.String(20))
    )
    


def downgrade():
    op.drop_table('mapping')
