"""empty message

Revision ID: 0eb1d6faa3c8
Revises: None
Create Date: 2016-08-11 16:00:48.444794

"""

# revision identifiers, used by Alembic.
revision = '0eb1d6faa3c8'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_name', sa.String(length=80), nullable=True),
    sa.Column('book_author', sa.String(length=120), nullable=True),
    sa.Column('book_status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('book_name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    ### end Alembic commands ###
