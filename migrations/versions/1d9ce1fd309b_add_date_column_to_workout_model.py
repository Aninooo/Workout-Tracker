"""Add date column to Workout model

Revision ID: 1d9ce1fd309b
Revises: 
Create Date: 2024-04-06 17:49:06.081427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d9ce1fd309b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout', schema=None) as batch_op:
        batch_op.drop_column('date')

    # ### end Alembic commands ###
