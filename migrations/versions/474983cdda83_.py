"""empty message

Revision ID: 474983cdda83
Revises: 3f0fbfe768c1
Create Date: 2014-11-22 23:51:27.043000

"""

# revision identifiers, used by Alembic.
revision = '474983cdda83'
down_revision = '3f0fbfe768c1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.String(length=256), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'title')
    ### end Alembic commands ###