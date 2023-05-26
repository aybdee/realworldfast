"""added title to articles

Revision ID: 8e31003cd57d
Revises: 974428a1a229
Create Date: 2023-05-25 23:53:03.427541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e31003cd57d'
down_revision = '974428a1a229'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('title', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'title')
    # ### end Alembic commands ###
