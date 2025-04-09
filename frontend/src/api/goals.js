import api from './axios';

export const getGoals = async () => {
  const res = await api.get('goals/');
  return res.data;
};

export const createGoal = async (name, targetAmount, currentAmount, deadline, notes) => {
  const res = await api.post('goals/', {
    name, target_amount: targetAmount, current_amount: currentAmount, deadline, notes
  });
  return res.data;
};

export const updateGoal = async (id, targetAmount, currentAmount, deadline, notes) => {
  const res = await api.put(`goals/${id}/`, {
    target_amount: targetAmount, current_amount: currentAmount, deadline, notes
  });
  return res.data;
};

export const deleteGoal = async (id) => {
  const res = await api.delete(`goals/${id}/`);
  return res.data;
};
