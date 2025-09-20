public class controlSatelite {
    // Definir constantes
    private static final double GRAVEDAD = 9.81; // en m/s^2
    private static final double RADIO_TIERRA = 6371; // en kilómetros
    private static final double KM = 1000.0; // Convertir kilómetros a metros
    private static final double HORAS = 1.0; // Una hora

    private float distanciaDeLaTierra;
    private float velocidadMedia;
    private float tiempoDeLaTierra;

    // Método para determinar el estado del satélite en términos de órbita
    private String estadoSatelite() {
        if (distanciaDeLaTierra < 1000) {
            return "El satélite está en una órbita baja.";
        } else if (distanciaDeLaTierra >= 1000 && distanciaDeLaTierra < 35000) {
            return "El satélite está en una órbita media.";
        } else {
            return "El satélite está en una órbita alta.";
        }
    }

    // Método que valida que los valores sean positivos
    public boolean validarValores(float distanciaDeLaTierra, float velocidadMedia, float tiempoDeLaTierra) {
        return distanciaDeLaTierra >= 0 && velocidadMedia >= 0 && tiempoDeLaTierra >= 0;
    }

    // Método para calcular la velocidad media
    public float calcularVelocidad(float distanciaDeLaTierra, float tiempoDeLaTierra) {
        velocidadMedia = distanciaDeLaTierra / tiempoDeLaTierra;
        return velocidadMedia;
    }

    // Método para calcular la distancia recorrida
    public float calcularDistancia(float velocidadMedia, float tiempoDeLaTierra) {
        distanciaDeLaTierra = velocidadMedia * tiempoDeLaTierra;
        return distanciaDeLaTierra;
    }

    // Método para calcular el tiempo estimado
    public float calcularTiempo(float distanciaDeLaTierra, float velocidadMedia) {
        tiempoDeLaTierra = distanciaDeLaTierra / velocidadMedia;
        return tiempoDeLaTierra;
    }

    // Método para calcular la aceleración debido a la gravedad en la Tierra
    public double calcularGravedad(double distancia) {
        final double G = 6.67430e-11; // Constante gravitacional en m^3·kg^−1·s^−2
        double masaTierra = 5.972e24; // Masa de la Tierra en kg
        return G * masaTierra / (distancia * distancia); // Fórmula de la ley de gravitación universal
    }
}
