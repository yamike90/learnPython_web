"""added email to user

Revision ID: 1408b8b8e66b
Revises: 138896ff32ec
Create Date: 2019-10-30 17:06:14.930128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1408b8b8e66b'
down_revision = '138896ff32ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###