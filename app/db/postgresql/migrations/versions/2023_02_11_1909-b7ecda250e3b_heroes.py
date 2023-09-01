"""heroes

Revision ID: b7ecda250e3b
Revises: 
Create Date: 2023-02-11 19:09:30.185682+00:00

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "b7ecda250e3b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "hrs_heroes",
        sa.Column("nickname", sa.String(length=255), nullable=False),
        sa.Column(
            "role",
            postgresql.ENUM(
                "mage",
                "assassin",
                "warrior",
                "priest",
                "tank",
                name="hrs_roles",
            ),
            nullable=False,
        ),
        sa.Column("deleted_at", sa.TIMESTAMP(), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "uuid",
            sa.UUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("uuid", name=op.f("pk__hrs_heroes")),
    )
    op.create_index(
        op.f("ix__hrs_heroes__nickname"),
        "hrs_heroes",
        ["nickname"],
        unique=True,
    )
    op.create_index(
        op.f("ix__hrs_heroes__uuid"), "hrs_heroes", ["uuid"], unique=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix__hrs_heroes__uuid"), table_name="hrs_heroes")
    op.drop_index(op.f("ix__hrs_heroes__nickname"), table_name="hrs_heroes")
    op.drop_table("hrs_heroes")
    # ### end Alembic commands ###

    op.execute("DROP TYPE hrs_roles;")