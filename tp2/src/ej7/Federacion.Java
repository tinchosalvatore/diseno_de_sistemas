package ej7;
import java.util.List;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor

public class Federacion {
    private List<Estacion> estaciones;   // lo agregue porque la Federacion regula estaciones
    private String nombre;
    private int cantFeredados;
}