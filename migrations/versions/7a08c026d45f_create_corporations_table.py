"""create corporations table

Revision ID: 7a08c026d45f
Revises: 
Create Date: 2020-09-16 13:12:35.551535

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '7a08c026d45f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'corporation',
        sa.Column('corp_num', postgresql.TEXT, primary_key=True),
        sa.Column('type', sa.String(length=40), nullable=False),
        sa.Column('recognition_date', sa.DateTime),
        sa.Column('bn15', postgresql.TEXT),
        sa.Column('email', postgresql.TEXT)
    )


def downgrade():
    op.drop_table('search')
