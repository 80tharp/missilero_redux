"""empty message

Revision ID: 5ad774dedc88
Revises: 3bb1892fe9c8
Create Date: 2022-06-30 10:38:11.468174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ad774dedc88'
down_revision = '3bb1892fe9c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('systems',
    sa.Column('system_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('system_name', sa.String(length=50), nullable=True),
    sa.Column('system_country', sa.String(length=50), nullable=True),
    sa.Column('system_range_class', sa.String(length=15), nullable=True),
    sa.Column('system_warhead', sa.String(length=15), nullable=True),
    sa.Column('system_range', sa.String(length=15), nullable=True),
    sa.Column('system_nuke_type', sa.String(length=15), nullable=True),
    sa.Column('system_launcher', sa.String(length=15), nullable=True),
    sa.Column('system_description', sa.Text(), nullable=True),
    sa.Column('system_image', sa.String(length=50), nullable=True),
    sa.Column('system_type', sa.String(length=50), nullable=True),
    sa.Column('system_status', sa.String(length=50), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('system_id')
    )
    op.drop_table('missiles')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('missiles',
    sa.Column('system_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('system_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('system_country', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('system_range_class', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('system_warhead', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('system_range', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('system_nuke_type', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('system_launcher', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('system_description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('system_image', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('system_type', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('system_status', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name='missiles_category_id_fkey'),
    sa.PrimaryKeyConstraint('system_id', name='missiles_pkey')
    )
    op.drop_table('systems')
    # ### end Alembic commands ###