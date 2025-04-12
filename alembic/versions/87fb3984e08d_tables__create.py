"""tables__create

Revision ID: 87fb3984e08d
Revises: 1064e087f23b
Create Date: 2025-02-27 14:17:05.685855

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "87fb3984e08d"
down_revision: Union[str, None] = "1064e087f23b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    conn = op.get_bind()
    if not conn.dialect.has_table(conn, "Categories"):
        op.create_table(
            "Categories",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("type", sa.String(), nullable=True),
            sa.Column("name", sa.String(), nullable=False),
            sa.PrimaryKeyConstraint("id"),
        )


def downgrade():
    op.drop_table("Categories")
