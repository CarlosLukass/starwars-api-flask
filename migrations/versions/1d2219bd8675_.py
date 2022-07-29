"""empty message

Revision ID: 1d2219bd8675
Revises: 8b348cb5fa6c
Create Date: 2022-07-29 01:23:27.337287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d2219bd8675'
down_revision = '8b348cb5fa6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('specie', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('hair_color', sa.String(length=20), nullable=False),
    sa.Column('skin_color', sa.String(length=20), nullable=False),
    sa.Column('eye_color', sa.String(length=20), nullable=False),
    sa.Column('birthyear', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('gender'),
    sa.UniqueConstraint('gender'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('specie'),
    sa.UniqueConstraint('specie')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('gravity', sa.String(length=20), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=20), nullable=False),
    sa.Column('terrain', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('gravity'),
    sa.UniqueConstraint('gravity'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('population'),
    sa.UniqueConstraint('population'),
    sa.UniqueConstraint('terrain'),
    sa.UniqueConstraint('terrain')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('average_height', sa.Integer(), nullable=False),
    sa.Column('average_lifespan', sa.Integer(), nullable=False),
    sa.Column('hair_colors', sa.String(length=20), nullable=False),
    sa.Column('eye_colors', sa.String(length=20), nullable=False),
    sa.Column('homewold', sa.String(length=20), nullable=False),
    sa.Column('language', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('average_height'),
    sa.UniqueConstraint('average_height'),
    sa.UniqueConstraint('average_lifespan'),
    sa.UniqueConstraint('average_lifespan'),
    sa.UniqueConstraint('eye_colors'),
    sa.UniqueConstraint('eye_colors'),
    sa.UniqueConstraint('hair_colors'),
    sa.UniqueConstraint('hair_colors'),
    sa.UniqueConstraint('homewold'),
    sa.UniqueConstraint('homewold'),
    sa.UniqueConstraint('language'),
    sa.UniqueConstraint('language'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('model', sa.String(length=20), nullable=False),
    sa.Column('starship_class', sa.String(length=20), nullable=False),
    sa.Column('manufacturer', sa.String(length=20), nullable=False),
    sa.Column('cost_in_credits', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cost_in_credits'),
    sa.UniqueConstraint('cost_in_credits'),
    sa.UniqueConstraint('manufacturer'),
    sa.UniqueConstraint('manufacturer'),
    sa.UniqueConstraint('model'),
    sa.UniqueConstraint('model'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('starship_class'),
    sa.UniqueConstraint('starship_class')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('model', sa.String(length=20), nullable=False),
    sa.Column('vehicle_class', sa.String(length=20), nullable=False),
    sa.Column('manufacturer', sa.String(length=20), nullable=False),
    sa.Column('cost_in_credits', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cost_in_credits'),
    sa.UniqueConstraint('cost_in_credits'),
    sa.UniqueConstraint('manufacturer'),
    sa.UniqueConstraint('manufacturer'),
    sa.UniqueConstraint('model'),
    sa.UniqueConstraint('model'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('vehicle_class'),
    sa.UniqueConstraint('vehicle_class')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    op.drop_table('starships')
    op.drop_table('species')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
