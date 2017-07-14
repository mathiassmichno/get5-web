"""empty message

Revision ID: d14fe2819dea
Revises: 07fc1ddd31cc
Create Date: 2017-07-14 18:14:49.330282

"""

# revision identifiers, used by Alembic.
revision = 'd14fe2819dea'
down_revision = '07fc1ddd31cc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('match', sa.Column('challonge_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_match_challonge_id'), 'match', ['challonge_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_match_challonge_id'), table_name='match')
    op.drop_column('match', 'challonge_id')
    # ### end Alembic commands ###
