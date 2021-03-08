"""empty message

Revision ID: 099d60caff0c
Revises: 
Create Date: 2021-03-08 20:49:22.472111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '099d60caff0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('region',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('region')
    # ### end Alembic commands ###