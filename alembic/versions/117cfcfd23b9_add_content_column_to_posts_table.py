"""add content column to posts table

Revision ID: 117cfcfd23b9
Revises: 46561467df72
Create Date: 2023-07-05 12:47:36.101325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '117cfcfd23b9'
down_revision = '46561467df72'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
