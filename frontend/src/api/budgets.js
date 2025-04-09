import api from './axios';

export const getBudgets = async () => {
  const res = await api.get('budgets/');
  return res.data;
};

export const createBudget = async (category, amount, month) => {
  const res = await api.post('budgets/', { category, amount, month });
  return res.data;
};

export const updateBudget = async (id, amount) => {
  const res = await api.put(`budgets/${id}/`, { amount });
  return res.data;
};

export const deleteBudget = async (id) => {
  const res = await api.delete(`budgets/${id}/`);
  return res.data;
};
