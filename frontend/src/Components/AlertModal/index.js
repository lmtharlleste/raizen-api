import React from 'react';
import './style.css'; // Estilos para o modal

const AlertModal = ({ title, message, onConfirm, onCancel }) => {
  return (
    <div className="modal-overlay">
      <div className="modal-container">
        <h2>{title}</h2>
        <p>{message}</p>
        <div className="modal-buttons">
          <button onClick={onConfirm} className="modal-button confirm">
            OK
          </button>
          <button onClick={onCancel} className="modal-button cancel">
            Cancelar
          </button>
        </div>
      </div>
    </div>
  );
};

export default AlertModal;
