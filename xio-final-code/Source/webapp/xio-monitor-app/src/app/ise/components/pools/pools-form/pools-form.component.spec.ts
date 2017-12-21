import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PoolsFormComponent } from './pools-form.component';

describe('PoolsFormComponent', () => {
  let component: PoolsFormComponent;
  let fixture: ComponentFixture<PoolsFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PoolsFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PoolsFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
