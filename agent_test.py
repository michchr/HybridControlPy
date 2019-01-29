from models.agents import Agent, MpcAgent
from utils.matrix_utils import block_toeplitz_alt, block_toeplitz
from models.micro_grid_agents import DewhModel, Dewh, GridModel
from models.mld_model import MldModel, MldInfo, MldSystemModel
from utils.structdict import StructDict, SortedStructDict
from models.parameters import dewh_p, grid_p
from tools.grid_dataframe import MicroGridDataFrame, MicroGridSeries
from numpy.lib.stride_tricks import as_strided as _as_strided
import cvxpy as cvx

from tools.mpc_tools import *

import scipy.sparse as scs
import scipy.linalg as scl
import numpy as np
import wrapt
import functools

dewh_model = DewhModel(param_struct=dewh_p)

num_devices = 100
grid_model = GridModel(num_devices=num_devices, param_struct=grid_p)


a = dict.fromkeys(MldModel._field_names, np.random.rand(3, 3))
a.update(b5=np.ones((3, 1)), d5=np.ones((3, 1)), f5=np.ones((3, 1)))
a.update(A=np.random.rand(3, 3), B2=None, D2=None, F2=None)

agent_model2 = MldSystemModel(MldModel(a, nu_l=1))

mld = dewh_model.get_mld_numeric(dewh_p)


agent = MpcAgent('dewh', None, dewh_model, N_p=96)
agent2= MpcAgent('test', None, agent_model2, N_p=96)
agent_g = MpcAgent('grid', None, grid_model, N_p=96)


# mld3 = MldModel(D1=1,D2=3,D3=2,D4=4,d5=6)
# agent3 = MpcAgent(agent_model=AgentModel(mld3), N_p=5)
# agent3._mpc_evo_gen.gen_state_input_evolution_matrices(96)


# con_mats = agent.gen_cons_evolution_matrices(96)
# opt_var_struct = agent._gen_optimization_vars(96)
# V_N_p = opt_var_struct.V_tilde_N_p
# V_N_cons = opt_var_struct.V_tilde_N_cons
# W = np.random.randint(3000,size=(97,1))
#
#
#
#
# obj = cvx.Minimize(cvx.sum(V_N_p))
# cons = [con_mats.H_V@V_N_cons <= con_mats.H_5+con_mats.H_W@W+con_mats.H_x*40]
# prob = cvx.Problem(obj,cons)
# # prob.solve(verbose=True)
#
# obj2 = cvx.Minimize(cvx.quad_form(V_N_p, np.eye(V_N_p.shape[0])) + cvx.sum(V_N_p))
# cons2 = [con_mats.H_V@V_N_cons <= con_mats.H_5+con_mats.H_W@W+con_mats.H_x*40]
# prob2 = cvx.Problem(obj2,cons2)
# # prob.solve(verbose=True)


#
# shape = (2,3)
# a = np.arange(1,np.prod(shape)+1)
# b = np.arange(a[-1]+1, a[-1]+np.prod(shape)+1)
# c = np.arange(b[-1]+1, b[-1]+np.prod(shape)+1)
# d =  np.arange(c[-1]+1, c[-1]+np.prod(shape)+1)
# e =  np.arange(d[-1]+1, d[-1]+np.prod(shape)+1)
# f =  np.arange(e[-1]+1, e[-1]+np.prod(shape)+1)
#
# a = a.reshape(shape)
# b = b.reshape(shape)
# c = c.reshape(shape)
# d = d.reshape(shape)
# e = e.reshape(shape)
# f = f.reshape(shape)
#
# col = np.array([a,b,c])
# row=np.array([c,d,e,f])
