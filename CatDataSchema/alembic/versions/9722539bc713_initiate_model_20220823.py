"""Initiate model 20220823

Revision ID: 9722539bc713
Revises: cfa0ebc93b1e
Create Date: 2022-08-23 16:24:11.378087

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9722539bc713'
down_revision = 'cfa0ebc93b1e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cat_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('entry', sa.DateTime(), nullable=True),
    sa.Column('depart', sa.DateTime(), nullable=True),
    sa.Column('duration', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table('cat_data')

