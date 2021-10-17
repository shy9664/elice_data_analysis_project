"""empty message

Revision ID: a8987895243c
Revises: 02d3b5698405
Create Date: 2021-10-13 15:28:16.429261

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a8987895243c'
down_revision = '02d3b5698405'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'file')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('file', mysql.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###
