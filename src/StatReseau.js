import './StatReseau.css';

function StatReseau({ lignes }) {
  const totalLignes = lignes.length;
  const totalArrets = lignes.reduce((sum, l) => sum + l.arrets, 0);
  const ligneMax = lignes.reduce((max, l) => l.arrets > max.arrets ? l : max, lignes[0]);

  return (
    <div className="stat-reseau">
      <div className="stat-item">
        <span className="stat-nombre">{totalLignes}</span>
        <span className="stat-label">Lignes</span>
      </div>
      <div className="stat-item">
        <span className="stat-nombre">{totalArrets}</span>
        <span className="stat-label">Arrêts au total</span>
      </div>
      <div className="stat-item">
        <span className="stat-nombre">Ligne {ligneMax.numero}</span>
        <span className="stat-label">Plus d'arrêts ({ligneMax.arrets})</span>
      </div>
    </div>
  );
}

export default StatReseau;