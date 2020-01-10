"""empty message

Revision ID: e2292e0fe35b
Revises: 4eee7ab22ef4
Create Date: 2020-01-10 11:11:53.936413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2292e0fe35b'
down_revision = '4eee7ab22ef4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('slug', sa.String(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('slug')

    # ### end Alembic commands ###
