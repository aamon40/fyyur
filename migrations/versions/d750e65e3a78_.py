"""empty message

Revision ID: d750e65e3a78
Revises: 78b4e669fd85
Create Date: 2022-06-03 02:22:19.573866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd750e65e3a78'
down_revision = '78b4e669fd85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show', 'artist_image_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('artist_image_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
