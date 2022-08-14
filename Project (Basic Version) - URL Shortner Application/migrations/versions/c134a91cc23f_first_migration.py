"""First Migration

Revision ID: c134a91cc23f
Revises: 
Create Date: 2022-08-14 22:38:34.184962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c134a91cc23f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urlshortener',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('baseurl', sa.String(length=500), nullable=False),
    sa.Column('shorten_url', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('urlshortener')
    # ### end Alembic commands ###
