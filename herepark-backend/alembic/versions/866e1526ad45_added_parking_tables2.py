"""Added parking tables2

Revision ID: 866e1526ad45
Revises: f11bcd77d6c2
Create Date: 2024-02-12 22:43:31.534285

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '866e1526ad45'
down_revision: Union[str, None] = 'f11bcd77d6c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spaces',
    sa.Column('space_id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('reservation_limit', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('space_id')
    )
    op.create_table('ratings',
    sa.Column('rating_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('space_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['space_id'], ['spaces.space_id'], ),
    sa.PrimaryKeyConstraint('rating_id')
    )
    op.create_table('reservations',
    sa.Column('reservation_id', sa.Integer(), nullable=False),
    sa.Column('reservation_datetime', sa.DateTime(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('space_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['space_id'], ['spaces.space_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('reservation_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservations')
    op.drop_table('ratings')
    op.drop_table('spaces')
    # ### end Alembic commands ###