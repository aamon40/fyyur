"""empty message

Revision ID: 4c6440251d22
Revises: 3c8ed72493fe
Create Date: 2022-06-04 08:19:40.628621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c6440251d22'
down_revision = '3c8ed72493fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('artist_image_link', sa.String(length=1000), nullable=True),
    sa.Column('start_time', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('image_unique', 'artist', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('image_unique', 'artist', ['image_link'])
    op.drop_table('show')
    # ### end Alembic commands ###
