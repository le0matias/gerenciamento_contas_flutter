"""empty message

Revision ID: 698ba7ac2f60
Revises: 8432e3944557
Create Date: 2022-12-12 09:06:38.778714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '698ba7ac2f60'
down_revision = '8432e3944557'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operacao', sa.Column('conta_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'operacao', 'conta', ['conta_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'operacao', type_='foreignkey')
    op.drop_column('operacao', 'conta_id')
    # ### end Alembic commands ###
