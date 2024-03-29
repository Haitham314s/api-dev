"""add last few columns to posts table

Revision ID: e0b8cd5e84cf
Revises: 41c330bb58c0
Create Date: 2023-01-19 21:11:19.728159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0b8cd5e84cf'
down_revision = '41c330bb58c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ("NOW()")),)
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
