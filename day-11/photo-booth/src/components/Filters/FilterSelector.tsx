// FilterSelector component for selecting AR filters
import type { FilterConfig } from '../../types/filters';

interface FilterSelectorProps {
  filters: FilterConfig[];
  selectedFilter: string | null;
  onFilterSelect: (filterId: string | null) => void;
  className?: string;
}

export function FilterSelector({ 
  filters, 
  selectedFilter, 
  onFilterSelect, 
  className = '' 
}: FilterSelectorProps) {
  return (
    <div className={`filter-selector ${className}`}>
      <h3>Choose Filter</h3>
      <div className="filter-selector__grid">
        {/* No filter option */}
        <button
          className={`filter-button ${!selectedFilter ? 'filter-button--active' : ''}`}
          onClick={() => onFilterSelect(null)}
        >
          <div className="filter-button__preview">
            <span className="filter-button__icon">✨</span>
          </div>
          <span className="filter-button__name">None</span>
        </button>

        {/* Filter options */}
        {filters.map(filter => (
          <button
            key={filter.id}
            className={`filter-button ${selectedFilter === filter.id ? 'filter-button--active' : ''}`}
            onClick={() => onFilterSelect(filter.id)}
          >
            <div className="filter-button__preview">
              <span className="filter-button__icon">{filter.icon}</span>
            </div>
            <span className="filter-button__name">{filter.name}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
