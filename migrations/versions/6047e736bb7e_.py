"""empty message

Revision ID: 6047e736bb7e
Revises: 
Create Date: 2020-03-06 15:33:29.250959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6047e736bb7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caixa',
    sa.Column('id_pagamento', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_pagamento')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('caixa')
    # ### end Alembic commands ###
