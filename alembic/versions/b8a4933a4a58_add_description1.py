"""add description1

Revision ID: b8a4933a4a58
Revises: dea73fa39b06
Create Date: 2023-06-23 16:15:01.911993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8a4933a4a58'
down_revision = 'dea73fa39b06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_subcategory',
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('subcategory_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['subcategory_id'], ['subcategory.id'], )
    )
    op.drop_table('article_subscription')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_subscription',
    sa.Column('article_id', sa.INTEGER(), nullable=True),
    sa.Column('subcategory_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['subcategory_id'], ['subcategory.id'], )
    )
    op.drop_table('article_subcategory')
    # ### end Alembic commands ###
