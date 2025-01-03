"""empty message

Revision ID: 628a9b3bfa2c
Revises: 
Create Date: 2024-12-22 19:53:37.038958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '628a9b3bfa2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sem', sa.Integer(), nullable=False),
    sa.Column('student', sa.Integer(), nullable=False),
    sa.Column('disc_name', sa.Integer(), nullable=False),
    sa.Column('goal', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_goals'))
    )
    op.create_table('plan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spec_name', sa.String(length=200), nullable=False),
    sa.Column('disc_name', sa.String(length=200), nullable=False),
    sa.Column('sem', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('exam', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_plan'))
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_roles')),
    sa.UniqueConstraint('role_name', name=op.f('uq_roles_role_name'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=200), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('middle_name', sa.String(length=50), nullable=True),
    sa.Column('form', sa.String(length=50), nullable=False),
    sa.Column('date', sa.Integer(), nullable=False),
    sa.Column('group', sa.String(length=50), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name=op.f('fk_users_role_id_roles'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('login', name=op.f('uq_users_login'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('plan')
    op.drop_table('goals')
    # ### end Alembic commands ###
