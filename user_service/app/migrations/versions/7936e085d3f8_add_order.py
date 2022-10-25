"""Add order

Revision ID: 7936e085d3f8
Revises: bafa6af1c9cf
Create Date: 2022-10-25 17:34:22.197308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7936e085d3f8'
down_revision = 'bafa6af1c9cf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('idempotent_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('idempotent_key', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_idempotent_request_id'), 'idempotent_request', ['id'], unique=False)
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_idempotent_request_id'), table_name='idempotent_request')
    op.drop_table('idempotent_request')
    # ### end Alembic commands ###