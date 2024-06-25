import 'bootstrap/dist/css/bootstrap.css';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/js/bootstrap';
import Header from './components/Header'; 

function App() {
  return (
    <>
      <Header/>
      <main className='container mt-5'>
        {/* Latest Products */}
        <div>
          <div className='d-flex justify-content-between'>
            <h3>Latest Products</h3>
            <a href="#" className='btn btn-dark'>All Products <i class="bi bi-arrow-right"></i></a>
          </div>
          <div className="row mt-4">
            {/* Card Item */}
            <div className="col-12 col-md-3 mb-3">
              <div className="card">
                <img src={logo} alt="logo" />
                <div className="card-body">
                  <h5 className="card-title">Card title</h5>
                  <p className='text-muted'>Price: Rs. 400</p>
                </div>
                <div className='card-footer'>
                  <button className='btn btn-warning me-2'><i class="bi bi-cart-plus"></i></button>
                  <button className='btn btn-danger'><i class="bi bi-heart"></i></button>
                </div>
              </div>
            </div>
            {/* Card End */}
            {/* Card Item */}
            <div className="col-12 col-md-3 mb-3">
              <div className="card">
                <img src={logo} alt="logo" />
                <div className="card-body">
                  <h5 className="card-title">Card title</h5>
                  <p className='text-muted'>Price: Rs. 400</p>
                </div>
                <div className='card-footer'>
                  <button className='btn btn-warning me-2'><i class="bi bi-cart-plus"></i></button>
                  <button className='btn btn-danger'><i class="bi bi-heart"></i></button>
                </div>
              </div>
            </div>
            {/* Card End */}
            {/* Card Item */}
            <div className="col-12 col-md-3 mb-3">
              <div className="card">
                <img src={logo} alt="logo" />
                <div className="card-body">
                  <h5 className="card-title">Card title</h5>
                  <p className='text-muted'>Price: Rs. 400</p>
                </div>
                <div className='card-footer'>
                  <button className='btn btn-warning me-2'><i class="bi bi-cart-plus"></i></button>
                  <button className='btn btn-danger'><i class="bi bi-heart"></i></button>
                </div>
              </div>
            </div>
            {/* Card End */}
            {/* Card Item */}
            <div className="col-12 col-md-3 mb-3">
              <div className="card">
                <img src={logo} alt="logo" />
                <div className="card-body">
                  <h5 className="card-title">Card title</h5>
                  <p className='text-muted'>Price: Rs. 400</p>
                </div>
                <div className='card-footer'>
                  <button className='btn btn-warning me-2'><i class="bi bi-cart-plus"></i></button>
                  <button className='btn btn-danger'><i class="bi bi-heart"></i></button>
                </div>
              </div>
            </div>
            {/* Card End */}
            {/* Card Item */}
            <div className="col-12 col-md-3 mb-3">
              <div className="card">
                <img src={logo} alt="logo" />
                <div className="card-body">
                  <h5 className="card-title">Card title</h5>
                  <p className='text-muted'>Price: Rs. 400</p>
                </div>
                <div className='card-footer'>
                  <button className='btn btn-warning me-2'><i class="bi bi-cart-plus"></i></button>
                  <button className='btn btn-danger'><i class="bi bi-heart"></i></button>
                </div>
              </div>
            </div>
            {/* Card End */}
            {/* Card Item */}
            <div className="col-12 col-md-3 mb-3">
              <div className="card">
                <img src={logo} alt="logo" />
                <div className="card-body">
                  <h5 className="card-title">Card title</h5>
                  <p className='text-muted'>Price: Rs. 400</p>
                </div>
                <div className='card-footer'>
                  <button className='btn btn-warning me-2'><i class="bi bi-cart-plus"></i></button>
                  <button className='btn btn-danger'><i class="bi bi-heart"></i></button>
                </div>
              </div>
            </div>
            {/* Card End */}
          </div>
        </div>
        {/* Latest Products End */}

      </main>
    </>
  );
}

export default App;

