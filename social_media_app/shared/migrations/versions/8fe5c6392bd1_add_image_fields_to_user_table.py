"""Add image fields to User table

Revision ID: 8fe5c6392bd1
Revises: 6fdfe1a7ed39
Create Date: 2024-10-15 19:09:05.274220

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8fe5c6392bd1'
down_revision = '6fdfe1a7ed39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_images')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_filename', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('image_uploaded_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('image_uploaded_at')
        batch_op.drop_column('image_filename')

    op.create_table('user_images',
    sa.Column('image_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('image_filename', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('uploaded_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='user_images_ibfk_1'),
    sa.PrimaryKeyConstraint('image_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
