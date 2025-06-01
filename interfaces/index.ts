export interface CardProps {
  children: React.ReactNode;
  // Add more properties as needed, such as:
  // title?: string;
  // image?: string;
  // price?: number;
  // rating?: number;
}

export interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'small' | 'medium' | 'large';
  disabled?: boolean;
}