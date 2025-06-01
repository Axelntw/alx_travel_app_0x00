import React from 'react';
import { ButtonProps } from '../../interfaces';

const Button: React.FC<ButtonProps> = ({ 
  children, 
  onClick, 
  variant = 'primary',
  size = 'medium',
  disabled = false 
}) => {
  const baseStyles = "font-medium rounded focus:outline-none";
  
  const variantStyles = {
    primary: "bg-red-500 hover:bg-red-600 text-white",
    secondary: "bg-gray-200 hover:bg-gray-300 text-gray-800",
    outline: "border border-red-500 text-red-500 hover:bg-red-50"
  };
  
  const sizeStyles = {
    small: "py-1 px-3 text-sm",
    medium: "py-2 px-4",
    large: "py-3 px-6 text-lg"
  };
  
  const classes = `${baseStyles} ${variantStyles[variant]} ${sizeStyles[size]} ${disabled ? 'opacity-50 cursor-not-allowed' : ''}`;
  
  return (
    <button 
      className={classes}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
};

export default Button;