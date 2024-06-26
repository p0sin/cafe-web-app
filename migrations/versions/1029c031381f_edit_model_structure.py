"""edit model structure

Revision ID: 1029c031381f
Revises: b5bf4ee38764
Create Date: 2024-04-05 11:07:53.293992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1029c031381f'
down_revision = 'b5bf4ee38764'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cafes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('map_url', sa.String(length=500), nullable=False))
        batch_op.add_column(sa.Column('image_url', sa.String(length=500), nullable=False))
        batch_op.alter_column('location',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cafes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=500), nullable=False))
        batch_op.alter_column('location',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=500),
               existing_nullable=False)
        batch_op.drop_column('image_url')
        batch_op.drop_column('map_url')

    # ### end Alembic commands ###
