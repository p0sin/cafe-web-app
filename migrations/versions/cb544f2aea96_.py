"""empty message

Revision ID: cb544f2aea96
Revises: 
Create Date: 2024-04-01 17:59:51.028718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb544f2aea96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cafes',
    sa.Column('cafe_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('location', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('cafe_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cafes')
    # ### end Alembic commands ###
