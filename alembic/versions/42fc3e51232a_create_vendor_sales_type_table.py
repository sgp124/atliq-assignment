"""create Vendor Sales Type table

Revision ID: 42fc3e51232a
Revises: 
Create Date: 2020-08-09 15:07:50.270390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42fc3e51232a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'vendor_transactions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date', sa.DateTime),
        sa.Column('cost', sa.String(20)),
        sa.Column('imei', sa.Numeric),
        sa.Column('phone', sa.Numeric),
    )
    pass


def downgrade():
    op.drop_table('vendor_transactions')
    pass
