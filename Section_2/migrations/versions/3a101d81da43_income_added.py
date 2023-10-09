"""income added

Revision ID: 3a101d81da43
Revises: fde519c5191e
Create Date: 2023-10-03 13:13:32.030117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a101d81da43'
down_revision = 'fde519c5191e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('income',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('expense', schema=None) as batch_op:
        batch_op.drop_column('expense_type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expense', schema=None) as batch_op:
        batch_op.add_column(sa.Column('expense_type', sa.BOOLEAN(), nullable=True))

    op.drop_table('income')
    # ### end Alembic commands ###