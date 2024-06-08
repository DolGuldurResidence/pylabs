import numpy as np
from scipy.stats import multivariate_normal
import time


def multivariate_normal_logpdf(X, m, C):
    D = m.shape[0]
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    norm_term = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)
    centered_X = X - m
    exponent = -0.5 * np.einsum('ij,ji->i', centered_X @ inv_C, centered_X.T)  # использование einsum для вычисления скалярных произведений
    log_pdf = norm_term + exponent
    return log_pdf

m = np.array([0, 0])
C = np.array([[1, 0.5], [0.5, 1]])
X = np.random.randn(100, 2)
log_pdf_custom = multivariate_normal_logpdf(X, m, C)

start_time = time.time()
log_pdf_custom = multivariate_normal_logpdf(X, m, C)
custom_time = time.time() - start_time
print(f"Custom implementation time: {custom_time}")

start_time = time.time()
log_pdf_scipy = multivariate_normal(m, C).logpdf(X)
scipy_time = time.time() - start_time
print(f"Scipy implementation time: {scipy_time}")

print(f"Maximum absolute difference: {np.max(np.abs(log_pdf_custom - log_pdf_scipy))}")