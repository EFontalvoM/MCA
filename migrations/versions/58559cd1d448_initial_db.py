"""Initial_db

Revision ID: 58559cd1d448
Revises: 
Create Date: 2022-10-31 07:30:14.623109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58559cd1d448'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('perfiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombrePerfil', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_prv',
    sa.Column('auto', sa.String(), nullable=True),
    sa.Column('auto_color', sa.String(), nullable=True),
    sa.Column('auto_modelo', sa.Integer(), nullable=True),
    sa.Column('auto_tipo', sa.Integer(), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('cantidad_compras_realizadas', sa.Integer(), nullable=True),
    sa.Column('codigo_zip', sa.String(), nullable=True),
    sa.Column('color_favorito', sa.Integer(), nullable=True),
    sa.Column('credit_card_num_cypher', sa.String(), nullable=True),
    sa.Column('cuenta_numero', sa.String(), nullable=True),
    sa.Column('direccion', sa.String(), nullable=True),
    sa.Column('fec_alta', sa.String(), nullable=True),
    sa.Column('fec_birthday', sa.String(), nullable=True),
    sa.Column('foto_dni', sa.String(), nullable=True),
    sa.Column('geo_latitud', sa.String(), nullable=True),
    sa.Column('geo_longitud', sa.String(), nullable=True),
    sa.Column('ip', sa.String(), nullable=True),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('agent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('apiKey', sa.String(), nullable=True),
    sa.Column('perfil', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['perfil'], ['perfiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_agent_email'), 'agent', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_agent_email'), table_name='agent')
    op.drop_table('agent')
    op.drop_table('users_prv')
    op.drop_table('perfiles')
    # ### end Alembic commands ###
