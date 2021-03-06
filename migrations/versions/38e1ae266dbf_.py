"""upstream.domain_id

Revision ID: 38e1ae266dbf
Revises: 567ffa3f5475
Create Date: 2014-10-09 14:32:45.157538

"""

# revision identifiers, used by Alembic.
revision = '38e1ae266dbf'
down_revision = '567ffa3f5475'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('upstream', sa.Column('domain_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('upstream', 'domain_id')
    ### end Alembic commands ###
