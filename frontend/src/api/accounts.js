import api from './axios';

export const getAccounts = async () => {
  const res = await api.get('accounts/');
  return res.data;
};

export const createAccount = async (name, type, balance, institution) => {
  const res = await api.post('accounts/', {
    name,
    type,
    balance,
    institution,
  });
  return res.data;
};
