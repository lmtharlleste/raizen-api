import React, { useRef } from 'react';
import './style.css';

const colors = [
  "#FF5733", "#33FF57", "#3357FF", "#F0E130", "#FF33A1", "#33FFF6", 
  "#F033FF", "#F7A833", "#FF5733", "#33FF57", "#3357FF", "#F0E130", 
  "#FF33A1", "#33FFF6", "#F033FF", "#F7A833", "#FF5733", "#33FF57", 
  "#3357FF", "#F0E130", "#FF33A1", "#33FFF6", "#F033FF", "#F7A833"
];

const HorizontalList = () => {
  const listRef = useRef(); // Referência para a lista de cores

  // Função para rolar a lista para a direita
  const scrollRight = () => {
    if (listRef.current) {
      listRef.current.scrollBy({ left: 100, behavior: 'smooth' });
    }
  };

  // Função para rolar a lista para a esquerda
  const scrollLeft = () => {
    if (listRef.current) {
      listRef.current.scrollBy({ left: -100, behavior: 'smooth' });
    }
  };

  return (
    <div className="list-container">
      <button className="scroll-button left" onClick={scrollLeft}>◀</button>

      <div className="horizontal-list" ref={listRef}>
        {colors.map((color, index) => (
          <div 
            key={index} 
            className="color-box" 
            style={{ backgroundColor: color, marginRight: index === colors.length - 1 ? '50px' : '0' }}
          />
        ))}
      </div>

      <button className="scroll-button right" onClick={scrollRight}>▶</button>
    </div>
  );
};

export default HorizontalList;
