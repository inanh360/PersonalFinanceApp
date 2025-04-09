import api from './axios';

// Fetch reports
export const getReports = async () => {
  const res = await api.get('reports/');
  return res.data;
};

// Create a report
export const createReport = async (reportType, data) => {
  const res = await api.post('reports/', { report_type: reportType, data });
  return res.data;
};

// Update a report
export const updateReport = async (id, reportType, data) => {
  const res = await api.put(`reports/${id}/`, { report_type: reportType, data });
  return res.data;
};

// Delete a report
export const deleteReport = async (id) => {
  const res = await api.delete(`reports/${id}/`);
  return res.data;
};
