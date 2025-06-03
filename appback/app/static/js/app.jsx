function App() {
  const [name, setName] = React.useState('');
  const [pass, setPass] = React.useState('');
  const [res, setRes] = React.useState('en attente');

  const handleSubmit = async () => {
    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, pass }),
      });

      if (!response.ok) {
        throw new Error('Erreur lors de l’envoi');
      }

      const data = await response.json();
      setRes(data?.result);
    } catch (error) {
      console.error('Erreur :', error);
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl mb-2">Formulaire de contact</h2>
      <input
        type="text"
        placeholder="Nom"
        value={name}
        onChange={(e) => setName(e.target.value)}
        className="border p-2 mb-2 w-full"
      />
      <input
        type="pass"
        placeholder="pass"
        value={pass}
        onChange={(e) => setPass(e.target.value)}
        className="border p-2 mb-2 w-full"
      />
      <button
        onClick={handleSubmit}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Envoyer
      </button>
      <h2 className="text-xl mb-2">{res}</h2>
    </div>
  );
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
  